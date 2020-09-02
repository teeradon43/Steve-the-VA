import 'package:flutter/material.dart';

var str = "";
class BgColor extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Center(
        child: Container(
            color: Colors.pink[100],
            width: 300,
            height: 200,
            child: Center(
                child: Text(str, style: TextStyle(fontSize: 40.0)))));
  }
}
Widget largeButton(){
  return Center(
    child: RaisedButton(
      onPressed: (){
        str = 'Yo Dude WTF';
        print('Click');
      }
    ),
  );
}
void main() {
  print('Running');
  runApp(MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        appBar: AppBar(
          title: Text('Hello, Steve'),
        ),
        body: Column(
          children: <Widget>[
            BgColor(),
            largeButton()
          ])
      )));
}
