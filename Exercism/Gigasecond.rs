use std::io;
use chrono::{NaiveDateTime, Duration};

fn add_seconds(data_input: &str) -> String {
    let format = "%Y-%m-%d %H:%M:%S";

    match NaiveDateTime::parse_from_str(data_input, format) {
        Ok(date) => {
            let future_date = date + Duration::seconds(1_000_000_000);
            future_date.format(format).to_string()
        },
        Err(_) => {
            "Invalid format".to_string()
        }
    }
}

fn main() {
    let mut input_date = String::new();

    io::stdin().read_line(&mut input_date).expect("There was an error reading the string");

    //sem isso aqui não funciona
    let input_date = input_date.trim();

    let future_date = add_seconds(input_date);
    println!("{}", future_date);
}
