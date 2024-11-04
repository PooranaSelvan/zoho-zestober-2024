function verifyPassport(passport) {
     // 1. Length Check
     if (passport.length < 10) {
       return "Invalid"
     }
   
     // 2. Nationality Check
     const nationalityCode = passport.substring(0, 3)
     if (!/^[A-Z]{3}$/.test(nationalityCode)) {
       return "Invalid"
     }
   
     // 3. Passport Number Check
     const passportNumber = passport.substring(3, 12)
     if (!/^\d{9}$/.test(passportNumber)) {
       return "Invalid"
     }
   
     // 4. Expiration Date Check
     const dateMatch = passport.match(/\d{4}-\d{2}-\d{2}/)
     if (!dateMatch) {
       return "Invalid"
     }
     
     const expirationDate = new Date(dateMatch[0])
     const today = new Date()
     if (isNaN(expirationDate.getTime()) || expirationDate < today) {
       return "Invalid"
     }
   
     // 5. Special Character Check
     const specialChars = /[!@#$%^&*()_+=~-]/
     if (!specialChars.test(passport)) {
       return "Invalid"
     }
   
     // 6. No Spaces Check
     if (passport.includes(' ')) {
       return "Invalid"
     }
   
     // 7. Issuing Authority Check
     const authorities = ['GOV', 'EMB', 'CONS']
     if (!authorities.some(auth => passport.includes(auth))) {
       return "Invalid"
     }
   
     return "Valid"
}
   
// Test cases
console.log(verifyPassport("USA1234567892025-12-31!GOV"))