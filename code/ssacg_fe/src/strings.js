export const pagetitle = {
    logIn:      "Iniciar sesión",
    signUp:     "Registrarse",
    main:       "ssacg | galería", 
    products:   "ssacg | productos",
};

let domain = "http://127.0.0.1:8000/";
const prod_domain = "https://ssacg-bkend.herokuapp.com/";
domain = prod_domain;

export const URLs = {
    logIn:  domain + "login/",
    refreshToken: domain + "refresh/",
    signUpAdmin: domain + "user/admin",
    existsEmail: domain + "user/byemail/",
  
    insertProduct:   domain + "user/product/",
    getAllProducts:  domain + "user/product/show/",
    get1Product:     domain + "user/product/view/",
    updateProduct:   domain + "user/product/update/",
    deleteProduct:   domain + "user/product/delete/",
};
