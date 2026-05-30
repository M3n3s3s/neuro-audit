import { Terminal } from '@xterm/xterm';
import { TerminalAdapter } from './terminal_adapter.js';
export class TerminalAdapter {
    constructor(divId, enterCallBack) {
        this.terminal = new Terminal({
            theme: {
                background: '#000000',
                foreground: '#39FF14'
            }
        });

        this.terminal.open(document.getElementById(divId));
        this.onEnterCallback = enterCallBack;
        this.comandoAtual = "";

        this.terminal.onData((tecla) => {
            if (tecla === '\r') {
                this.terminal.write('\r\n');
                if (typeof this.onEnterCallback === 'function') {
                    this.onEnterCallback(this.comandoAtual);
                }
                this.comandoAtual = "";
            } else if (tecla === '\x7f') {
                if (this.comandoAtual.length > 0) {
                    this.comandoAtual = this.comandoAtual.slice(0, -1);
                    this.terminal.write('\b \b');
                }
            } else {
                this.comandoAtual += tecla;
                this.terminal.write(tecla);
            }
        });
    }

    print(texto){
        this.terminal.write(texto);
    }

    printLine(texto){
        this.terminal.write(texto + '\r\n');
    }

    printPrompt(){
        this.terminal.write('$ ');
    } 
}