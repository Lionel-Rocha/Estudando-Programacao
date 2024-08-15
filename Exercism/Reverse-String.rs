use std::io;

fn invert_string(data_input: & String) -> String {
    let mut inverted = String::new();
    let mut data_copy = data_input.to_string(); 
    while let Some(c) = data_copy.pop() {
        inverted.push(c);
    } //particularmente achei esse código uma piada de mau gosto

    inverted
}

fn main(){
    let mut input_string = String::new();
    io::stdin().read_line(&mut input_string).expect("Erro ao ler string");
    let inverted = invert_string(&input_string);
    println!("{}", inverted);
}
