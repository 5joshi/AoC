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
    let input: &str = include_str!("../../inputs/day04.txt");

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

struct BingoBoard(Vec<(u32, bool)>);

impl BingoBoard {
    fn new(input: &str) -> Self {
        Self(
            input
                .lines()
                .map(|line| line.split_whitespace().map(|n| (n.parse().unwrap(), false)))
                .flatten()
                .collect::<Vec<_>>(),
        )
    }

    fn get(&self, x: u32, y: u32) -> (u32, bool) {
        self.0[(x * 5 + y) as usize]
    }

    fn mark(&mut self, num: u32) {
        if let Some(pos) = self.0.iter().position(|&elem| elem == (num, false)) {
            self.0[pos].1 = true;
        }
    }

    fn bingo(&self) -> bool {
        for x in 0..5 {
            if (0..5).all(|y| self.get(x, y).1) || (0..5).all(|y| self.get(y, x).1) {
                return true;
            }
        }

        false
    }

    fn sum_unmarked_numbers(&self) -> u32 {
        self.0
            .iter()
            .fold(0, |total, (num, b)| total + num * (!b) as u32)
    }
}

fn part1(input: &str) -> u32 {
    let mut split_input = input.split("\n\n");
    let nums = split_input
        .next()
        .unwrap()
        .split(',')
        .map(|s| s.parse().unwrap())
        .collect::<Vec<_>>();
    let mut boards = split_input.map(|s| BingoBoard::new(s)).collect::<Vec<_>>();
    for num in nums {
        for board in boards.iter_mut() {
            board.mark(num);
            if board.bingo() {
                return board.sum_unmarked_numbers() * num;
            }
        }
    }
    panic!()
}

fn part2(input: &str) -> u32 {
    let mut split_input = input.split("\n\n");
    let nums = split_input
        .next()
        .unwrap()
        .split(',')
        .map(|s| s.parse().unwrap())
        .collect::<Vec<_>>();
    let mut boards = split_input.map(|s| BingoBoard::new(s)).collect::<Vec<_>>();
    for num in nums {
        boards.retain(|b| !b.bingo());
        let length = boards.len();
        for board in boards.iter_mut() {
            board.mark(num);
            if length == 1 && board.bingo() {
                return board.sum_unmarked_numbers() * num;
            }
        }
    }
    panic!()
}
