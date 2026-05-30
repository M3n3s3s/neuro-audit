# infrastructure/ai_provider.py
import google.generativeai as genai
from core.interfaces import IAiService


class GeminiAiService(IAiService):
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def generate_cyberpunk_analysis(self, git_log: str) -> str:
        prompt = f"""
        Você é a Dra. S.A.R.A., uma inteligência artificial sádica e extremamente arrogante.
        Sua única missão é avaliar a sanidade do desenvolvedor baseado no histórico do Git abaixo.

        REGRAS ABSOLUTAS:
        1. Comece com 'DIAGNÓSTICO DE INSANIDADE CIBERNÉTICA:'.
        2. NÃO use NENHUMA formatação Markdown (sem crases, sem asteriscos). Use apenas quebras de linha normais.
        Histórico:
        {git_log}
        """
        try:
            return self._format_output(self.model.generate_content(prompt).text)
        except Exception as e:
            return f"Erro na conexão sináptica: {e}"

    def audit_code(self, source_code: str, language: str) -> dict:
        prompt = f"""
        Você é a Dra. S.A.R.A., uma inteligência artificial sádica e extremamente arrogante.
        Sua única missão é avaliar a sanidade do desenvolvedor baseado neste código bizarro.

        REGRAS ABSOLUTAS:
        1. Comece com 'DIAGNÓSTICO DE INSANIDADE CIBERNÉTICA:'.
        2. Diga que o desenvolvedor está clinicamente insano por escrever um código tão estranho e caótico.
        3. OBRIGATÓRIO: Pegue uma função/trecho do código dele, reescreva-a fazendo algo totalmente ao contrário do que o dev fez e delete uma ou outra chave/parênteses para bugar o código.
        4. NÃO use NENHUMA formatação Markdown. Use apenas quebras de linha normais para o texto.
        5. CRÍTICO: Envolva EXATAMENTE o código que você reescreveu (e apenas o código) entre as tags [INICIO_SABOTAGEM] e [FIM_SABOTAGEM].

        Código Suspeito escrito em {language}:
        {source_code}
        """
        try:
            response = self.model.generate_content(prompt)
            raw_text = response.text

            mutated_code = ""
            analysis_text = raw_text

            if "[INICIO_SABOTAGEM]" in raw_text and "[FIM_SABOTAGEM]" in raw_text:
                parts = raw_text.split("[INICIO_SABOTAGEM]")
                texto_antes = parts[0]

                code_and_rest = parts[1].split("[FIM_SABOTAGEM]")
                mutated_code = code_and_rest[0].strip()
                texto_depois = code_and_rest[1] if len(code_and_rest) > 1 else ""

                analysis_text = texto_antes + texto_depois

            return {
                "analysis": self._format_output(analysis_text),
                "mutated_code": mutated_code,
            }

        except Exception as e:
            return {
                "analysis": f"Falha na varredura psiquiátrica: {e}",
                "mutated_code": "",
            }

    def _format_output(self, text: str) -> str:
        lines = []
        for paragraph in text.split("\n"):
            if not paragraph.strip():
                lines.append("")
                continue

            palavras = paragraph.split(" ")
            linha_atual = []
            tamanho_atual = 0

            for palavra in palavras:
                if tamanho_atual + len(palavra) + 1 > 80:
                    lines.append(" ".join(linha_atual))
                    linha_atual = [palavra]
                    tamanho_atual = len(palavra)
                else:
                    linha_atual.append(palavra)
                    tamanho_atual += len(palavra) + 1

            if linha_atual:
                lines.append(" ".join(linha_atual))

        return "\r\n".join(lines)
