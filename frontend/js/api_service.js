class ApiService{

    
     static async get(endpoint) {
        try{
            const Response = await fetch(endpoint)
            
            const data = await Response.json();

            return data;
        }catch(error){
            console.log('Ocorreu um erro:')
        }
    }
    

    static async  post(endpoint, payload){
        try{
            const Response = await fetch(endpoint, {
                method: 'POST',
                headers:{
                    'Content-Type': 'application/json'
                },
                BODY: JSON.stringify(payload)
            })

            const dados = await Response.JSON();

            return data;


         } catch (error) {
            console.log('Ocorreu um erro:', error);
        }
    }
    
}

export default ApiService;