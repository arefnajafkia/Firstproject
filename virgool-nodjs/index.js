const express = require('express');

const app = express();


app.get("/",(req,res)=>{

    res.send("This is root");
});

app.get("/users",(req,res)=>{

});



app .listen(3000,()=>{
    console.log("server is ready on port 3000");
})