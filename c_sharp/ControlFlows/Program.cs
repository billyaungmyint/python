namespace ControlFlows
{
    public enum ShippingMethod
    {
        RegularAirMail = 1,
        RegisteredAirMail = 2,
        Express = 3

    }
    internal class Program
    {
        static void Main(string[] args)
        {
            var method = ShippingMethod.RegularAirMail;
            Console.WriteLine((int)method);

            var methodId = 3;
            Console.WriteLine((ShippingMethod)methodId);
        }
    }
}