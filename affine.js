  var charmap = {
          a : 1,
          b : 2,
          c : 3,
          d : 4,
          e : 5,
          f : 6,
          g : 7,
          h : 8,
          i : 9,
          j : 10,
          k : 11,
          l : 12,
          m : 13,
          n : 14,
          o : 15,
          p : 16,
          q : 17,
          r : 18,
          s : 19,
          t : 20,
          u : 21,
          v : 22,
          w : 23,
          x : 24,
          y : 25,
          z : 26
  };
    
    var charmap_reverse = {
          1 : "a",
          2 : "b",
          3 : "c",
          4 : "d",
          5 : "e",
          6 : "f",
          7 : "g",
          8 : "h",
          9 : "i",
          10 : "j",
          11 : "k",
          12 : "l",
          13 : "m",
          14 : "n",
          15 : "o",
          16 : "p",
          17 : "q",
          18 : "r",
          19 : "s",
          20 : "t",
          21 : "u",
          22 : "v",
          23 : "w",
          24 : "x",
          25 : "y",
          26 : "z"
  };

    
  var inv = {1: 1, 3: 9, 5: 21, 7: 15, 9: 3, 11: 19, 15: 7, 17: 23, 19: 11, 21: 5, 23: 17, 25: 25};

  var my_text;
        
my_text = "XIBKGLTIZKSBKIRLIGLGSVNLWVIMZTVDZHVUUVXGREVOBHBMLMBNLFHDRGSVMXIBKGRLMGSVXLMEVIHRLMLURMULINZGRLMUILNZIVZWZYOVHGZGVGLZKKZIVMGMLMHVMHVGSVLIRTRMZGLILUZMVMXIBKGVWNVHHZTVHSZIVWGSVWVXLWRMTGVXSMRJFVMVVWVWGLIVXLEVIGSVLIRTRMZORMULINZGRLMLMOBDRGSRMGVMWVWIVXRKRVMGHGSVIVYBKIVXOFWRMTFMDZMGVWKVIHLMHGLWLGSVHZNVHRMXVDLIOWDZIRZMWGSVZWEVMGLUGSVXLNKFGVIGSVNVGSLWHFHVWGLXZIIBLFGXIBKGLOLTBSZEVYVXLNVRMXIVZHRMTOBXLNKOVCZMWRGHZKKORXZGRLMNLIVDRWVHKIVZWNLWVIMXIBKGLTIZKSBRHSVZEROBYZHVWLMNZGSVNZGRXZOGSVLIBZMWXLNKFGVIHXRVMXVKIZXGRXVXIBKGLTIZKSRXZOTLIRGSNHZIVWVHRTMVWZILFMWXLNKFGZGRLMZOSZIWMVHHZHHFNKGRLMHNZPRMTHFXSZOTLIRGSNHSZIWGLYIVZPRMKIZXGRXVYBZMBZWEVIHZIBRGRHGSVLIVGRXZOOBKLHHRYOVGLYIVZPHFXSZHBHGVNYFGRGRHRMUVZHRYOVGLWLHLYBZMBPMLDMKIZXGRXZONVZMHGSVHVHXSVNVHZIVGSVIVULIVGVINVWXLNKFGZGRLMZOOBHVXFIVGSVLIVGRXZOZWEZMXVHVTRNKILEVNVMGHRMRMGVTVIUZXGLIRAZGRLMZOTLIRGSNHZMWUZHGVIXLNKFGRMTGVXSMLOLTBIVJFRIVGSVHVHLOFGRLMHGLYVXLMGRMFZOOBZWZKGVW";

text = my_text.toLowerCase();    
 
function dene(a,b) { 

    var a;
    var b;
    var arr = [];
    
    for(var i = 0; i < text.length; i++) {
        var c = (charmap[text[i]] - b) % 26;
        if (c < 0) 
		{
            c = c + 26;
        }
        if (c == 0) 
		{
            c = 26;
        }
        var y = (inv[a] * c) % 26;
        if (y == 0) 
		{
             y=26;
        }
        if( y < 0 ) 
		{
             y = y + 26;
        }
        arr.push(charmap_reverse[y]);
        }
    var z = arr.join("");
    console.log(z); 
    
    
}


for(i=1;i<25;i++) {
    
    console.log("new line a=1 -- b = " + i);
    console.log("--------");
    dene(1,i);
    console.log("new line a=3 -- b = " + i);
    console.log("--------");
    dene(3,i);
    console.log("new line a=5 -- b = " + i);
    console.log("--------");
    dene(5,i);
    console.log("new line a=7 -- b = " + i);
    console.log("--------");
    dene(7,i);
    console.log("new line a=9 -- b = " + i);
    console.log("--------");
    dene(9,i);
    console.log("new line a=11 -- b = " + i);
    console.log("--------");
    dene(11,i);
    console.log("new line a=15 -- b = " + i);
    console.log("--------");
    dene(15,i);
    console.log("new line a=17 -- b = " + i);
    console.log("--------");
    dene(17,i);
    console.log("new line a=19 -- b = " + i);
    console.log("--------");
    dene(19,i);
    console.log("new line a=21 -- b = " + i);
    console.log("--------");
    dene(21,i);
    console.log("new line a=23 -- b = " + i);
    console.log("--------");
    dene(23,i);
    console.log("new line a=25 -- b = " + i);
    console.log("--------");
    dene(25,i);
}


