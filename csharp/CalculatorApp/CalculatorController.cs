
using Microsoft.AspNetCore.Mvc;
using System.Diagnostics;

namespace CalculatorApp.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class CalculatorController : ControllerBase
    {
        [HttpPost]
        public ActionResult<string> Calculate([FromBody] CalculationRequest req)
        {
            var process = new Process
            {
                StartInfo = new ProcessStartInfo
                {
                    FileName = "dotnet",
                    Arguments = $"run --project CalculatorApp/CalculatorApp.csproj {req.Operation} {req.Num1} {req.Num2}",
                    RedirectStandardOutput = true,
                    UseShellExecute = false,
                    CreateNoWindow = true,
                }
            };
            process.Start();
            string result = process.StandardOutput.ReadToEnd();
            process.WaitForExit();
            return result;
        }
    }

    public class CalculationRequest
    {
        public string Operation { get; set; }
        public double Num1 { get; set; }
        public double Num2 { get; set; }
    }
}
