# prison-riddle

<a href = "https://www.youtube.com/watch?v=iSNsgj1OCLA"> The Riddle That Seems Impossible Even If You Know The Answer </a> from <a href = "https://www.youtube.com/c/veritasium"> Veritasium </a>

![Screen Shot 2022-06-30 at 17 46 57](https://user-images.githubusercontent.com/45129483/176775491-1aaa6b2d-c4fb-4df6-b682-4627c968215a.png)

If the chosen startegy is to randomly choose the boxes, the probability that all prisioners find their numbers is extremely low, lower than two people picking out the same grain of sand all over the world. This probability would be (1/2)^100

Another stategy:

- Boxes are in loops
- If you start with the box that has your number, the loop will end with your number, but it can have different lengths. 
- If the size of the loop is shorter than 51, you will find your number. In case it is 51 or bigger, they will lose
- So, if all the loops are shorter than 51, all the prisoners will escape. 
- In this case, we have to calculate the probability that all loops have the length 50 or less


P(L = 100) = UNIQUE LOOPS / TOTAL PERMUTATIONS

UNIQUE LOOPS: 100!/100

TOTAL PERMUTATIONS: 100!

P(L = 100) = 1/100 = 0.01

P(L = 84) = 1/84 

P(L = 13) = 1/13 

![Screen Shot 2022-06-30 at 18 04 19](https://user-images.githubusercontent.com/45129483/176778062-4d2f7aa0-0c07-41a1-9aa8-02b2025d25da.png)

![Screen Shot 2022-06-30 at 18 08 11](https://user-images.githubusercontent.com/45129483/176778569-7769f230-fdcf-4f0a-b101-77a6f9f663d1.png)


### Hw do you know your number is on the loop?

You have to start you your number, because that is the only way to close the loop

### How to change only two numbers in the boxes and guarantee success for all prisioners?

Swap two numbers in order to make two loops shorter than 51

### Different number of prisioners

P(succes) = 1 - P(failure)


![Screen Shot 2022-06-30 at 18 17 07](https://user-images.githubusercontent.com/45129483/176779783-3790ecf4-a303-49c8-9531-597b1c9df36e.png)


![Screen Shot 2022-06-30 at 18 16 11](https://user-images.githubusercontent.com/45129483/176779646-c10f654b-1e1b-4b53-96c9-9d1dc65ce7d4.png)

