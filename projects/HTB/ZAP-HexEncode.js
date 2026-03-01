// script to use in ZAP for hex encoding
// to use, replace DECODED_CHARACTERS

function process(payload) {

    var base = "DECODED_CHARACTERS";
    var full = base + payload;

    // Base64 encode
    var b64 = org.apache.commons.codec.binary.Base64.encodeBase64String(
        new java.lang.String(full).getBytes()
    );

    // Convert Base64 to ASCII hex
    var hex = "";
    for (var i = 0; i < b64.length; i++) {
        hex += b64.charCodeAt(i).toString(16);
    }

    return hex;
}
