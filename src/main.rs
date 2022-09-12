pub mod input;
pub mod string_to_int;

use crate::input::input;
use crate::string_to_int::string_to_int;

fn mayan_calandar(baktun: u8, katun: u8, tun: u8, uninal: u8, kin: u8) -> u32 {
    let katun: u32 = katun as u32 + 20*(baktun as u32);
    let tun: u32 = tun as u32 +20*(katun as u32);
    let uninal: u32 = uninal as u32+18*(tun as u32);
    let kin: u32 = kin as u32 + 20*(uninal as u32);
    return kin as u32;
}

fn main() {
    let mayan_input = input("input: ");
    let mayan_split = mayan_input.trim().split(" ");
    const EPOCH:u32 = 2018843;
    let mut array: Vec<u8> = Vec::new();

    for s in mayan_split {
        array.push(string_to_int(s))
    }
    let current = mayan_calandar(array[0],array[1],array[2],array[3],array[4]);
    let differnece = current - EPOCH;
    let mut days = differnece as i32;
    let mut year: u16 = 2000;
    let mut month: &str;
    loop {
        month = "January";
        let remove = 31;
        if days - remove < 0 {break}
        days -= remove;

        month = "February";
        let mut remove = 28;
        if (year % 100 != 0 && year % 4 == 0) || (year % 400 == 0) {remove += 1}
        if days - remove < 0 {break}
        days -= remove;

        month = "March";
        let remove = 31;
        if days - remove < 0 {break}
        days -= remove;

        month = "April";
        let remove = 30;
        if days - remove < 0 {break}
        days -= remove;

        month = "May";
        let remove = 31;
        if days - remove < 0 {break}
        days -= remove;

        month = "June";
        let remove = 30;
        if days - remove < 0 {break}
        days -= remove;

        month = "July";
        let remove = 31;
        if days - remove < 0 {break}
        days -= remove;

        month = "August";
        let remove = 31;
        if days - remove < 0 {break}
        days -= remove;

        month = "September";
        let remove = 30;
        if days - remove < 0 {break}
        days -= remove;

        month = "October";
        let remove = 31;
        if days - remove < 0 {break}
        days -= remove;

        month = "November";
        let remove = 30;
        if days - remove < 0 {break}
        days -= remove;

        month = "December";
        let remove = 31;
        if days - remove < 0 {break}
        days -= remove;

        year += 1;
    }
    println!("{} {} {}", days+1, month, year)
}
