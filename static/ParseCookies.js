function cookieParse() {
    var H_MIN_SLIDER = document.getElementById("H_MIN");
    var H_MAX_SLIDER = document.getElementById("H_MAX");
    var S_MIN_SLIDER = document.getElementById("S_MIN");
    var S_MAX_SLIDER = document.getElementById("S_MAX");
    var V_MIN_SLIDER = document.getElementById("V_MIN");
    var V_MAX_SLIDER = document.getElementById("V_MAX");

    var cookieParse = document.cookie.split("=");

    if (cookieParse.length > 0) {
        var HSVBounds = [];
        for (var i=1; i < cookieParse.length; i++) {
            HSVBounds.push(cookieParse[i].split("; ")[0]);
        }

        h_min = HSVBounds[0];
        h_max = HSVBounds[1];
        s_min = HSVBounds[2];
        s_max = HSVBounds[3];
        v_min = HSVBounds[4];
        v_max = HSVBounds[5];

        H_MIN_SLIDER.value = h_min;
        H_MAX_SLIDER.value = h_max;
        S_MIN_SLIDER.value = s_min;
        S_MAX_SLIDER.value = s_max;
        V_MIN_SLIDER.value = v_min;
        V_MAX_SLIDER.value = v_max;
    }
};