use std::io;

fn string_to_int() -> i32{
    let mut input = String::new();

    println!("Enter an integer:");
    io::stdin().read_line(&mut input).expect("Failed to read line");

    let num: i32 = input.trim().parse().expect("Invalid input");

    return num;
}

fn gets_int_size(int_input: i32) -> i32 {
    let mut size = 1;

    let mut div_int = int_input;

    while div_int / 10 != 0 {
        size = size + 1;
        div_int = div_int / 10;
    }

    return size;
}

fn is_armstrong(int_input: i32) -> bool {

    //as u32 é a conversão necessária para usar o pow.
    let size = gets_int_size(int_input) as u32;
    let mut div_int = int_input;
    let mut div:i32 = 10;
    div = div.pow(size);
    let mut sum = 0;
    
    for i in 0..size+1{
        let v = div_int / div;
        div_int = div_int % div;
        div = div / 10;
        sum = sum + v.pow(size);
    }

    if sum == int_input{
      return true;  
    } else {
        return false;
    }  
}

fn main(){
    let input_number = string_to_int();
    let is_ams = is_armstrong(input_number);
    println!("{}",is_ams);
}
