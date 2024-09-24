//Honestamente esse foi o exercício mais difícil até agora. 

fn translate_to_pig(word: &str) -> String {
    let vowels = ['a', 'e', 'i', 'o', 'u'];
    let exceptions = ["xr", "yt"];

    let mut pig_latin = String::new();

    let (first_letter, rest) = word.split_at(1);
    let first_letter = first_letter.to_lowercase();

    let first_two =  &word[..2].to_lowercase();

    if vowels.contains(&first_letter.chars().next().unwrap_or(' ')) || exceptions.contains(&first_two.as_str()) {
        pig_latin.push_str(first_letter.as_str()); 
        pig_latin.push_str(rest); 
        pig_latin.push_str("ay"); 
    } else {

        pig_latin.push_str(rest);
        pig_latin.push_str(first_letter.as_str());
        pig_latin.push_str("ay");
        
    }

    return pig_latin; 
}

fn main() {
    let pig_word = translate_to_pig("xray");
    println!("{}", pig_word);
}
