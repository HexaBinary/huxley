from invoice_automation.src.handler.registration_handler import RegistrationHandler

# TODO: Change to prod versions before deployment
# sandbox
#CLIENT_ID = "ABYdHrqfKuQBK7bDiZpCK9C6Cq9bhayJJZbPCRyJLu7rO2nNqX"
#CLIENT_SECRET = "KKJQ9uQJdlydvcCZigkZ3PlbEXQ8ZUjohKrEwzjN"
#REFRESH_TOKEN = ""
# prod
CLIENT_ID = "AB6M8vUqtDAsPaooTFWYk81NztxLFyRQR2ms6B8IL3hkwBttp6"
CLIENT_SECRET = "wN2KDQA9X7fWTPpkOnO3U87g2dlZ7HRsxnRtv4Iq"
REFRESH_TOKEN = "AB11671571531dOzhApAw3hiXy8xT4B1pHMQTcVrF75RERYqAO"
REALM_ID = "1404322785"
ACCESS_TOKEN = "eyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..F-7GnjHFy15sB40dWOuJLQ.1Yuy4Mpz2c6O0iTQYc2XVCJ1c9nWb-uRyMGeeEspsciI8NmRJHb9AiUpd3GmDAciGQFDND4SPU-hn699sBcdTtFm6Z7E_-eJS9qvpzaLV72_7NXAaXsKgv7lZ2QpSVP10-QGycNrt9FAn3j51oXA5BWjwkbIs_6Iqiq2JAoXNUSfYyYJ2SEmuGlqpkOg1N6l8LmFtQvgO_ZbaY-lo1Jd4iPi9d7sOmkuB4Sf_ElQX8ZcY3McBWO1rAFNhedXQMQgQI1l3FSVNpfX0kL9C6siq2oPfG2B9fhXT163qI8Eof2W4UXFecn605N-xgED-FS_nVsHj_B_fHYtYdgVm5kOtzOPMvrW8M2_-NJLfuNh2ytH82Q8Abv3IFQgWv2pfddcDlOszMnmiEpTVkfZy9zg6ajO4X80Wia307E1MHn11pu3L9DUbZjM1IljK6RZw4G4aP5MFv7in8kE_EJzMR2hJ-JaeZlo4cLrH3ERfC-3T6U5z-BbXjOAdhNdG8zLRSrwbh1BrKsEWWYRXnvhs06hUz33vZjS-8ctqPJ8cL5m_2kujBvrE0OmRA-ckRnkIgQgSgE9qgZjSgZ_Sf5YgMwOgxchSpKkypU1Smt3znTzRPdzLXETML91LN-3erX1ILhYA-ZTGqDdMSm-HjZJbe6nnZLhD8yh8zTsTqfsDj7ra0N3jC402CTPs78KaUPspgTQxzTX20pJV5Ua7pWkzuzf-qLUH7SZgeb0Jv0cvjuV428.ViSoMsNL2myxba5s4c8btA"

handler = RegistrationHandler(CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN, REALM_ID, ACCESS_TOKEN)
print(handler)
