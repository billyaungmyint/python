namespace ControlFlows
{
    public class Person
    {
        public string FirstName { get; set; }
        public string LastName { get; set; }
        
        public void Introduce()
        {
            Console.WriteLine("Myy name is " + FirstName + " " + LastName);
        }
    }
}