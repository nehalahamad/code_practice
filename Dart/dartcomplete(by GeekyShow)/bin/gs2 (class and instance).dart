// # Class and Object
/*
class Class_name{
  class Member
}
*/
void main() {
  // Creating an Object
  var samsung = new Mobile(); // new is optional

  // Calling Instance Method using Object
  samsung.showModel("A 100");

  // Creating an Object
  var lg = Mobile();
  lg.showModel("L 200");

  // Accessing Instance Variable using Object
  print(lg.ram);

  // Accessing Static Variable using Class Name
  print(Mobile.memory);

  // Calling Static Method using Class Name
  var total_memory = Mobile.addExtraMemory(8);
  print(total_memory);
}

class Mobile {
  // Instance Variable
  String model;
  int ram = 4;

  // Instance Method
  showModel(md) {
    model = md;
    print(model);
  }

  /*
    The static keyword is used to declare a variable or method that belongs to the class, not the instances. 
    This means that the class has only one copy of that variable or method.
    It generally manages the memory for the global data variable. 
    The static variables and methods are the member of the class instead of an individual instance.
    **statics variable/method in Dart is like class variable/method in Python
  */

  // Static Variable
  static int memory = 12;

  // Static Method
  static addExtraMemory(extra) {
    memory = memory + extra;
    return memory;
  }
}
