
async function gets_word() {
    const response = await fetch('https://random-word-api.herokuapp.com/word');
    if (!response) {
        throw new Error('Network response was not ok');
    }
    const data = await response.json();
    return data[0];
}

function normalizeText(word) {
    return word
        .replace(/ã/g, 'a')
        .replace(/á/g, 'a')
        .replace(/â/g, 'a')
        .replace(/à/g, 'a')
        .replace(/ä/g, 'a')
        .replace(/é/g, 'e')
        .replace(/è/g, 'e')
        .replace(/ê/g, 'e')
        .replace(/ë/g, 'e')
        .replace(/í/g, 'i')
        .replace(/î/g, 'i')
        .replace(/ï/g, 'i')
        .replace(/ó/g, 'o')
        .replace(/ô/g, 'o')
        .replace(/õ/g, 'o')
        .replace(/ö/g, 'o')
        .replace(/ú/g, 'u')
        .replace(/û/g, 'u')
        .replace(/ü/g, 'u')
        .replace(/ç/g, 'c')
        .replace(/ñ/g, 'n');
}

async function generates_password() {

    try {
        let word1 = await gets_word();
        let word2 = await gets_word();

        word1 = normalizeText(word1);
        word2 = normalizeText(word2);

        let random = Math.floor(Math.random() * 990) + 1;

        let password = word1 + "_" + word2 + "_" + random.toString();

        document.getElementById("before").innerText = "Your new password is:"
        let password_show = document.getElementById("word");
        password_show.innerText = password;

    } catch (e) {
        let password_show = document.getElementById("word");
        password_show.innerText = e;
    }

}
