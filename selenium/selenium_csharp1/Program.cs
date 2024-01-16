using OpenQA.Selenium.DevTools.V115.Database;

namespace selenium_csharp1
{
    internal class Program
    {
        public void getData()
        {
            Console.WriteLine("I am inside the method");
        }
        static void Main(string[] args)
        {
            Program p =new Program();
            p.getData();

            Console.WriteLine("Hello, World!");
            int a = 4;
            Console.WriteLine("Number is : " + a);

            String name = "Billy";
            Console.WriteLine("Name is : " + name);

            Console.WriteLine($"Name is : {name}");

            var age = 23;
            Console.WriteLine($"age is : {age}");
            
        }
    }
}