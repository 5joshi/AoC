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
    let input: &str = include_str!("../../inputs/day03.txt");

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

fn common(input: &Vec<&str>) -> Vec<String> {
    let length = input.len() as u32;
    let mut lines = input.into_iter();
    let mut counts = lines
        .next()
        .unwrap()
        .chars()
        .map(|c| c.to_digit(10).unwrap())
        .collect::<Vec<_>>();
    for line in lines {
        for (idx, c) in line.chars().enumerate() {
            counts[idx] += c.to_digit(10).unwrap();
        }
    }

    counts
        .into_iter()
        .map(|n| (n as f32 >= (length as f32 / 2.0)) as u32)
        .map(|n| n.to_string())
        .collect::<Vec<_>>()
}

fn part1(input: &str) -> u32 {
    let gamma: String = common(&input.lines().collect::<Vec<_>>()).join("");
    let epsilon: String = gamma
        .chars()
        .map(|c| (c == '0') as u32)
        .map(|n| n.to_string())
        .collect::<Vec<_>>()
        .join("");

    u32::from_str_radix(&gamma, 2).unwrap() * u32::from_str_radix(&epsilon, 2).unwrap()
}

fn part2(input: &str) -> u32 {
    let mut idx = 0;
    let length = input.lines().next().unwrap().len();
    let mut oxygen_options: Vec<_> = input.lines().collect();
    let mut co2_options: Vec<_> = input.lines().collect();

    while oxygen_options.len() > 1 && idx < length {
        let most_common = common(&oxygen_options)[idx].chars().next().unwrap();
        oxygen_options.retain(|option| option.chars().nth(idx).unwrap() == most_common);
        idx += 1;
    }

    idx = 0;
    while co2_options.len() > 1 && idx < length {
        let most_common = common(&co2_options)[idx].chars().next().unwrap();
        if co2_options
            .clone()
            .into_iter()
            .any(|option| option.chars().nth(idx).unwrap() != most_common)
        {
            co2_options.retain(|option| option.chars().nth(idx).unwrap() != most_common);
        }
        idx += 1;
    }

    let oxygen = &oxygen_options[0];
    let co2 = &co2_options[0];

    u32::from_str_radix(&oxygen, 2).unwrap() * u32::from_str_radix(&co2, 2).unwrap()
}
