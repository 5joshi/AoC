use std::{error::Error, time::Instant};

fn main() {
    if let Err(err) = run() {
        eprintln!("Error: {}", err);
        let mut e: &dyn Error = &*err;

        while let Some(src) = e.source() {
            eprintln!("  - caused by: {}", src);
            e = src;
        }
    }
}

fn run() -> Result<(), Box<dyn Error>> {
    let start = Instant::now();
    let input: &str = include_str!("../../inputs/day01.txt");

    println!("Setup: {:?}", start.elapsed()); //

    let start = Instant::now();
    let p1 = part1(input);
    println!("Part 1: {} [{:?}]", p1, start.elapsed()); //

    let start = Instant::now();
    let p2 = part2(input);
    println!("Part 2: {} [{:?}]", p2, start.elapsed()); //

    // assert_eq!(p1, 0);
    // assert_eq!(p2, 0);

    Ok(())
}

fn part1(input: &str) -> u32 {
    input
        .lines()
        .zip(input.lines().skip(1))
        .fold(0, |x, (n1, n2)| {
            x + (n1.parse::<u32>().unwrap() < n2.parse::<u32>().unwrap()) as u32
        })
}

fn part2(input: &str) -> u32 {
    input
        .lines()
        .zip(input.lines().skip(3))
        .fold(0, |x, (n1, n2)| {
            x + (n1.parse::<u32>().unwrap() < n2.parse::<u32>().unwrap()) as u32
        })
}
