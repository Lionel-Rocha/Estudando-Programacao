use std::io;

//soma de cada número ao quadrado
fn square_one(int_input: i32) -> i32{
    let mut square_one = 0;

     for i in 1..int_input+1 {
         let power = i.pow(2);
         square_one += power;
     }
    
    return square_one;   
}

//quadrado da soma de cada número
fn square_two(int_input: i32) -> i32{
    let mut sum = 0;
    
    for i in 1..int_input+1 {
        sum += i;
    }
    
    let square_two = sum.pow(2);
    
    return square_two;
}

fn gets_input() -> i32{
    let mut input = String::new();
    println!("Insert a number: ");
    io::stdin().read_line(&mut input).expect("Failed to read line");

    let num: i32 = input.trim().parse().expect("Invalid input");
    return num;
}

fn main() {
    let num = gets_input();
    let first_square = square_one(num);
    let second_square = square_two(num);
    let difference = second_square - first_square;
    print!("{} - {} = {}", second_square, first_square, difference);
}
