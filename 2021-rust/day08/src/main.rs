use std::{
    collections::{BTreeSet, HashMap},
    error::Error,
    time::Instant,
};

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
    let input: &str = include_str!("../../inputs/day08.txt");

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
    let mut result: u32 = 0;
    for mut line in input.lines().map(|l| l.split(" | ")) {
        let output = line.nth(1).unwrap().split(' ');
        result += output.filter(|s| s.len() <= 4 || s.len() == 7).count() as u32;
    }

    result
}

fn part2(input: &str) -> u32 {
    let mut result: u32 = 0;
    for mut line in input.lines().map(|l| l.split(" | ")) {
        let mut data = line
            .next()
            .unwrap()
            .split(' ')
            .map(|s| s.chars().collect::<BTreeSet<_>>())
            .collect::<Vec<_>>();
        let output = line
            .next()
            .unwrap()
            .split(' ')
            .map(|s| s.chars().collect::<BTreeSet<_>>());
        data.sort_by_key(|s| s.len());
        let mut mapping = HashMap::new();

        mapping.insert(&data[0], 1);
        mapping.insert(&data[1], 7);
        mapping.insert(&data[2], 4);
        mapping.insert(&data[9], 8);

        let mut six_mapping = &BTreeSet::new();
        let mut nine_mapping = &BTreeSet::new();

        for num in &data[6..9] {
            if data[2].is_subset(num) {
                mapping.insert(num, 9);
                nine_mapping = num;
            } else if data[0].is_subset(num) {
                mapping.insert(num, 0);
            } else {
                mapping.insert(num, 6);
                six_mapping = num;
            }
        }

        for num in &data[3..6] {
            if six_mapping.is_superset(num) {
                mapping.insert(num, 5);
            } else if nine_mapping.is_superset(num) {
                mapping.insert(num, 3);
            } else {
                mapping.insert(num, 2);
            }
        }

        result += output
            .into_iter()
            .map(|n| mapping[&n].to_string())
            .collect::<Vec<_>>()
            .join("")
            .parse::<u32>()
            .unwrap()
    }

    result
}
