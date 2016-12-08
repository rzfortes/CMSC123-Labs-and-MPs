#include <windows.h>
#include <conio.h>
#include <iostream>
#include <fstream>
#include <stack>
#include <queue>
#include <typeinfo>

using namespace std;

// this class will be used lang to easily get the coordinates of the cell for solving
class location {
public:
  int row;
  int column;
  location();
  location(int x, int y) {
    row = x;
    column = y;
  }
};

class cell {
public:
  int row;
  int column;
  char item;
  bool visited;
  cell();
  cell(int, int, char);
};

cell::cell() {
  // do nothing
  row = 0;
  column = 0;
  visited = false;
}

cell::cell(int row, int column, char item) {
  this->row = row;
  this->column = column;
  this->item = item;
  visited = false;
}

template <class T>
class agenda {
public:
  T *adt;
  int type; // 1 for stack, 2 for queue
public:
  cell c;
  agenda();
  ~agenda() {
    delete adt;
  };
  void add(cell);
  bool remove();
  bool isEmpty();
  int getSize();
  cell peek();
};

template <class T>
agenda<T>::agenda() {
  adt = new T();
  string t1 = typeid(*adt).name();
  string t2 = typeid(stack<cell>).name();
  string t3 = typeid(queue<cell>).name();
  //cout << t1 << endl << t2 << endl;
  if(t1.compare(t2) == 0) {
    type = 1;
  } else if(t1.compare(t3) == 0) {
    type = 2;
  }
}

template <class T>
void agenda<T>::add(cell c) {
  if(type == 1) {
    adt->push(c);
  } else {
    adt->push(c);
  }
}
template <class T>
bool agenda<T>::remove() {
  if(type == 1) {
    adt->pop();
  } else {
    adt->pop();
  }
  return true;
}

template <class T>
bool agenda<T>::isEmpty() {
  if(adt->empty()) {
    return true;
  }
  return false;
}

template <class T>
int agenda<T>::getSize() {
  return adt->size();
}

template <class T>
cell agenda<T>::peek() {
  if(type == 1) {
    return adt->top();
  } else {
    return adt->top();
  }
}

class maze {
public:
  int row;
  int column;
  cell **arr;
  int start_row, start_column;
  int end_row, end_column;
  maze();
  maze(int, int);
  ~maze();
  void add(cell c);
  string toString();
};

maze::maze() {
  // do nothing
}

maze::maze(int row, int column) {
  this->row = row;
  this->column = column;
  arr = new cell*[row];
  for(int i = 0; i < row; i++) {
    arr[i] = new cell[column];
  }
}

maze::~maze() {
  for(int i = 0; i < row; i++) {
      delete[] arr[i];
  }
  delete[] arr;
}

void maze::add(cell c) {
  arr[c.row][c.column] = c;
  if(c.item == 'o') {
    start_row = c.row;
    start_column = c.column;
  } else if(c.item == '*') {
    end_row = c.row;
    end_column = c.column;
  }
}

string maze::toString() {
  string x = "";
  for(int i = 0; i < row; i++) {
    for(int j = 0; j < column; j++) {
      x += arr[i][j].item;
    }
    x += "\n";
  }
  return x;
}

template <class T>
class mazesolver {
private:
  agenda<T> *a;
  maze *m;
public:
  stack<cell> backtrack;
  mazesolver();
  mazesolver(agenda<T>*, maze*);
  ~mazesolver();
  void solve();
  void writesolution();
};

template <class T>
mazesolver<T>::mazesolver() {
  // do nothing
}

template <class T>
mazesolver<T>::mazesolver(agenda<T> *b, maze *n) {
  m = new maze(n->row, n->column);
  for(int i = 0; i < n->row; i++) {
    for(int j = 0; j < n->column; j++) {
      m->add(n->arr[i][j]);
      cout << m->arr[i][j].item << endl;
    }
  }
  m->start_row = n->start_row;
  m->start_column = n->start_column;
  m->end_row = n->end_row;
  m->end_column = n->end_column;
  m->row = n->row;
  m->column = n->column;

  a = new agenda<T>();

  a->adt = b->adt;
  a->type = b->type;
}

template <class T>
mazesolver<T>::~mazesolver() {

}

template <class T>
void mazesolver<T>::solve() {
  char path = '.';
  char exit = '*';
  int ctr;
  // start from the entrance
  location current_cell(m->start_row, m->start_column);
  // short cut to check if the current cell in maze is visited
  cout << "hello" << endl;
  do {

    ctr = 1;
    //cout << "before ifs" << endl;
    //cout << m->arr[m->start_row][m->start_column].item << endl;//"r: " << current_cell.row << " | c: " << current_cell.column << endl; //m->arr[current_cell.row][current_cell.column - 1].item << endl;
    // left
    if((m->arr[current_cell.row][current_cell.column - 1].item == path ||
       m->arr[current_cell.row][current_cell.column - 1].item == exit) &&
       m->arr[current_cell.row][current_cell.column - 1].visited == false) {
        if(m->arr[current_cell.row][current_cell.column - 1].item == exit) {
          break;
        }
        a->add(m->arr[current_cell.row][current_cell.column - 1]);
        ctr++;
        cout << "hello from left" << endl;
    }
    // up
    if((m->arr[current_cell.row - 1][current_cell.column].item == path ||
       m->arr[current_cell.row - 1][current_cell.column].item == exit) &&
       m->arr[current_cell.row - 1][current_cell.column].visited == false) {
        if(m->arr[current_cell.row - 1][current_cell.column].item == exit) {
          break;
        }
        a->add(m->arr[current_cell.row - 1][current_cell.column]);
        ctr++;
        cout << "hello from up" << endl;
    }
    // right
    if((m->arr[current_cell.row][current_cell.column + 1].item == path ||
       m->arr[current_cell.row][current_cell.column + 1].item == exit) &&
       m->arr[current_cell.row][current_cell.column + 1].visited == false) {
        if(m->arr[current_cell.row][current_cell.column + 1].item == exit) {
          break;
        }
        a->add(m->arr[current_cell.row][current_cell.column + 1]);
        ctr++;
        cout << "hello from right" << endl;
    }
    // down
    if((m->arr[current_cell.row + 1][current_cell.column].item == path ||
       m->arr[current_cell.row + 1][current_cell.column].item == exit) &&
       m->arr[current_cell.row + 1][current_cell.column].visited == false) {
        if(m->arr[current_cell.row + 1][current_cell.column].item == exit) {
          break;
        }
        a->add(m->arr[current_cell.row + 1][current_cell.column]);
        ctr++;
        cout << "hello from down" << endl;
    }

    // if char == '*', exit found; else backtrack
    if(current_cell.row == m->end_row && current_cell.column == m->end_column) {
      cout << "exit found!!!!!!!!!!!!!" << endl;
      break;
    }

    if(ctr == 1) { // meaning, dead end; so go back
      while(a->peek().row != backtrack.top().row && a->peek().column != backtrack.top().column) {
        m->arr[backtrack.top().row][backtrack.top().column].visited = false;
        backtrack.pop();
      }
      a->remove();
      backtrack.push(a->peek());
      current_cell.row = a->peek().row;
      current_cell.column = a->peek().column;
      m->arr[current_cell.row][current_cell.column].visited = true;
      cout <<  "hello from new path.. " << current_cell.row << " " << current_cell.column << " " <<endl;
    } else {
        backtrack.push(a->peek());
        current_cell.row = a->peek().row;
        current_cell.column = a->peek().column;
        m->arr[current_cell.row][current_cell.column].visited = true;
        cout <<  "hello from current path.. " << current_cell.row << " " << current_cell.column << " " <<endl;
    }
    //Sleep(1000);
  } while(ctr <= 4);
}

template <class T>
void mazesolver<T>::writesolution() {

  ofstream out("maze.out", ios::app);

  out << "\n\n";

  while(!backtrack.empty()) {
    //if(m->arr[backtrack.top().row][backtrack.top().column].item == '*') {
      //break;
    //} else{
      m->arr[backtrack.top().row][backtrack.top().column].item = 'x';
      backtrack.pop();
    //}

  }
  out << m->toString();
}

int main() {
  int testcases;
  int row;
  int column;

  ifstream file("maze.in");
  ofstream out("maze.out", ios::app);

  if(file.is_open()) {
    file>>testcases;
    while(!file.eof()) {
      file >> row;
      file >> column;
      // instance of a maze
      maze mazed(row, column);
      string st;
      for(int i = 0; i < row; i++) {
        file >> st;
        for(int j = 0; j < column; j++) {
          cell c;
          c.row = i;
          c.column = j;
          c.item = st[j];
          mazed.add(c);
        }
      }
      agenda<stack<cell> > a;
      agenda<queue<cell> > b;
      mazesolver<stack<cell> > ms(&a, &mazed);
      ms.solve();
      ms.writesolution();
      
      /* commented out due to some errors..
      
      mazesolver<queue<cell> > ms2(&b, &mazed);
      ms2.solve();
      mazesolver<queue<cell> > ms2(&b, &mazed);
      ms2.solve();
      create instance of a maze solver <queue>
      solve and write solution
      */
      
      if(file.eof()) {
        break;
      }
    }
  } file.close();

  return 0;
}
