const express = require('express')
const bodyParser = require('body-parser')
const axios = require('axios')
const app = express()
app.use(bodyParser.json())
const port = 3000

//http://127.0.0.1:5000/predict
app.post("/analyze-sentiment",(req,res)=>{
    const data = req.body
    if(!data.text){
        return res.status(400).send('sentiment text is required')
    }
    try{
        axios.post('http://127.0.0.1:5000/predict',{
            text:data.text
        }).then((response) =>{
            const sentiment = response.data.sentiment
            res.status(200).json({
                sentiment:sentiment
            })
        }).catch((error)=>{
            res.status(500).send('Error analyzing sentiment from Flask API')
        })
        
    }catch(error){
        res.status(500).send('Error analyzing sentiment from nodeJS API')
    }
})

app.listen(port,()=>{
    console.log('Server is running on port: '+port)
})
