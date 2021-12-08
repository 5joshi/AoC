use itertools::Itertools;
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
    let input: &str = include_str!("../../inputs/day02.txt");

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
    let mut horizontal = 0;
    let mut depth = 0;
    for line in input.lines() {
        match line.split(' ').next_tuple() {
            Some(("forward", num)) => horizontal += num.parse::<u32>().unwrap(),
            Some(("down", num)) => depth += num.parse::<u32>().unwrap(),
            Some(("up", num)) => depth -= num.parse::<u32>().unwrap(),
            _ => panic!(),
        }
    }

    horizontal * depth
}

fn part2(input: &str) -> u32 {
    let mut horizontal = 0;
    let mut depth = 0;
    let mut aim = 0;
    for line in input.lines() {
        match line.split(' ').next_tuple() {
            Some(("forward", num)) => {
                horizontal += num.parse::<u32>().unwrap();
                depth += num.parse::<u32>().unwrap() * aim;
            }
            Some(("down", num)) => aim += num.parse::<u32>().unwrap(),
            Some(("up", num)) => aim -= num.parse::<u32>().unwrap(),
            _ => panic!(),
        }
    }

    horizontal * depth
}
