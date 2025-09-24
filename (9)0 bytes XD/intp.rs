use std::io; 

fn main() {
    println!("Please enter some text:"); 
    let mut user_input = String::new();
    io::stdin()
        .read_line(&mut user_input)
        .expect("Failed to read line"); 
    let input = user_input.trim();
    if input == "0" {
        println!("0");
    }
    if input == "1" {
        while 7 == 7 {
            println!("1");
        }
    }
}