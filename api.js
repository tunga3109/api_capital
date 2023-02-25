const axios = require('axios');

const endpointUrl = 'https://api-capital.backend-capital.com';

// create the data object with username and password
const axiosInstance = axios.create({
endpointUrl,
headers: {
    'Content-Type': 'application/json',
    'Authorization': 'QjBjQRpkQ8Fxc9Os'
},
auth: {
    identifier: 'tunga3109@gmail.com',
    password: 'Xuxin_10031999' 
}
});
  
// make the POST request with Axios
axiosInstance.post('/api/v1/session', {})
.then(response => {
    // handle success
    console.log(response.data);
});
