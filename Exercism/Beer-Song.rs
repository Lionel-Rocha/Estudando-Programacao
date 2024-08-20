fn main(){
    
    for i in (0..100).rev(){
        if i > 1{
            println!("{} bottles of beer on the wall, {} bottles of beer.", i, i);
        } else if i == 1{
            println!("{} bottle of beer on the wall, {} bottle of beer.", i, i);
        } else {
            println!("No more bottles of beer on the wall, no more bottles of beer.");
        }
    
        if i == 1{
            println!("Take one down and pass it around, no more bottles of beer on the wall.");
        } else if i == 0 {
            println!("Go to the store and buy some more, 99 bottles of beer on the wall.");
        } else {
            println!("Take one down and pass it around,{} bottles of beer on the wall.", i-1);
        }
        
    }
}
