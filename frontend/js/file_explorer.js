import apiservice from "./api_service.js"

export class FileExplorer{
    
    async static list(){
      
        const array = await apiservice.get(endpoint)


        const container = document.getElementById('container')

    
        array.array.forEach(element => {
        
            const file = document.createElement('div')

            file.classList.add('card')

            const titulo = document.createElement('h2')

            titulo.TextContent = element.text;

            file.appendChild(titulo)

            container.appendChild(file)
        });

    }

}