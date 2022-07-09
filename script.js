let a = 5;

let b = [1, 2, 3, 4, 5, 6, 7, 8, 9];

let mul = () => {
  for (let i = 0; i < b.length; i++) {
    console.log(b[i] * a);
  }
};

mul();
