function cookieParse() {
    var H_MIN_SLIDER = document.getElementById("H_MIN");
    var H_MAX_SLIDER = document.getElementById("H_MAX");
    var S_MIN_SLIDER = document.getElementById("S_MIN");
    var S_MAX_SLIDER = document.getElementById("S_MAX");
    var V_MIN_SLIDER = document.getElementById("V_MIN");
    var V_MAX_SLIDER = document.getElementById("V_MAX");

    var cookieParse = document.cookie.split("; ");

    if (cookieParse.length > 0) {
        for (var i=0; i < cookieParse.length; i++) {
            cookieParse[i] = cookieParse[i].split("=");
            
            switch (cookieParse[i][0]) {
                case "H_MIN":
                    H_MIN_SLIDER.value = cookieParse[i][1];
                    break;
                case "H_MAX":
                    H_MAX_SLIDER.value = cookieParse[i][1];
                    break;
                case "V_MIN":
                    V_MIN_SLIDER.value = cookieParse[i][1];
                    break;
                case "V_MAX":
                    V_MAX_SLIDER.value = cookieParse[i][1];
                    break;
                case "S_MIN":
                    S_MIN_SLIDER.value = cookieParse[i][1];
                    break;
                case "S_MAX":
                    S_MAX_SLIDER.value = cookieParse[i][1];
                    break;
            }
        }
    }
};