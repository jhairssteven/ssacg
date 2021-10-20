export const pagetitle = {
    logIn:      "Iniciar sesión",
    signUp:     "Registrarse",
    main:       "ssacg | galería", 
    products:   "ssacg | productos",
};

const domain = "http://127.0.0.1:8000/";

export const URLs = {
    logIn:  domain + "login/",
    signUpAdmin: domain + "user/admin",
    existsEmail: domain + "user/byemail/",
  
    insertProduct:   domain + "user/product/",
    getAllProducts:  domain + "user/product/show/",
    get1Product:     domain + "user/product/view/",
    updateProduct:   domain + "user/product/update/",
    deleteProduct:   domain + "user/product/delete/",
};
