using System;
using System.ComponentModel.DataAnnotations;
using System.Drawing;

class Program
{
    static void Main(string[] args)
    {
        List<Shape> Shapes = new List<Shape>();

        Square square = new Square();
        square.SetSide(5);
        square.SetColor("Red");
        //Console.WriteLine($"Square Area: {square.GetArea()}");
        Shapes.Add(square);

        Rectangle rect = new Rectangle();
        rect.SetLength(4);
        rect.SetWidth(6);
        rect.SetColor("Blue");
        //Console.WriteLine($"Rectangle Area: {rect.GetArea()}");
        Shapes.Add(rect);

        Circle circle = new Circle();
        circle.SetRadius(3);
        circle.SetColor("Green");
        //Console.WriteLine($"Circle Area: {circle.GetArea()}");
        Shapes.Add(circle);

        foreach (Shape shape in Shapes)
        {
            Console.WriteLine($"{shape.GetType().Name} Color: {shape.GetColor()}, Area: {shape.GetArea()}");
        }

        

        
    }
    public class Shape
    {
        private string _color;

          public void SetColor(string Color)
        {
            _color = Color;
            
        }
        public string GetColor()
        {
            return _color;

        }

      

        public virtual double GetArea()
        {
            return -1;
        }
    }

    public class Square : Shape
    {
        private int _side;

        public void SetSide(int Side)
        {
            _side = Side;
        }
        public int GetSide()
        {
            
            return _side;
        }

        public override double GetArea()
        {
            return _side * _side;

        }

    }

    public class Rectangle : Shape
    {
        private int _length;
        private int _width;

        public void SetLength(int Length)
        {
            _length = Length;
        }

        public int GetRectangleLength()
        {
            
            return _length;
        }
              public void SetWidth(int Width)
        {
            
            _width = Width;
        }

        public int GetRectangleWidth()
        {
            
            return _width;
        }

        public override double GetArea()
        {
            return _length * _width;
        }
    }

    public class Circle : Shape
    {
        private int _radius;
        double Pi = Math.PI;

        public void SetRadius(int Radius)
        {
            _radius =Radius;
        }

        public int GetRadius() {
            return _radius;
        }
     

       
        public override double GetArea()
        {
            return Pi * _radius * _radius;
        }

    }
}