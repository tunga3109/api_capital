<?php
 
$curl = curl_init();

curl_setopt_array($curl, array(
 CURLOPT_URL => 'https://demo-api-capital.backend-capital.com/api/v1/session',
 CURLOPT_RETURNTRANSFER => true,
 CURLOPT_ENCODING => '',
 CURLOPT_MAXREDIRS => 10,
 CURLOPT_TIMEOUT => 0,
 CURLOPT_FOLLOWLOCATION => true,
 CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
 CURLOPT_CUSTOMREQUEST => 'POST',
 CURLOPT_POSTFIELDS =>'{
   "identifier": "tunga3109@gmail.com",
   "password": "Xuxin_10031999"
}',
 CURLOPT_HTTPHEADER => array(
  'X-CAP-API-KEY: BPDLOiaDtqJwVheD',
  'Content-Type: application/json'
 ),
));


// Extrag parameters not included in Capital.com to read
curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($curl, CURLOPT_HEADER, 1);
$response = curl_exec($curl);
curl_close($curl);
echo "<br>Antwort Neue Sitzung + Header<br> ".$response."<br><br>";

?>