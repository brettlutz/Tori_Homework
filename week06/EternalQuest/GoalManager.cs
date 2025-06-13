using System.ComponentModel;
using System.Formats.Asn1;
using MakingGoals;

namespace MakingGoals
{
    public abstract class GoalManager : Goal
    {
        protected List<Goal> goals = new List<Goal>();
        protected int totalPoints = 0;
        public void Start()
        {
            Console.WriteLine("Welcome to Eternal Quest");
            Console.WriteLine("Would you like to: ");
            Console.WriteLine("1. Create Goal");
            Console.WriteLine("2. List Goals");
            Console.WriteLine("3. Save Goals");
            Console.WriteLine("4. Load Goals");
            Console.WriteLine("5. Record Event");
            Console.WriteLine("6.Quit");
            string Answer = Console.ReadLine();

            if (Answer == "6")
            {
                Console.WriteLine("Goodbye");
                Environment.Exit(0);
            }
            else if (Answer == "1")
            {
                Console.WriteLine("What kind of goal is it?");
                Console.WriteLine("1. Simple Goal ");
                Console.WriteLine("2. Eternal Goal");
                Console.WriteLine("3. Checklist Goal");
                string GoalAnswer = Console.ReadLine();

                Goal newGoal = null;
                if (GoalAnswer == "1")
                {
                    newGoal = new SimpleGoal();

                }
                else if (GoalAnswer == "2")
                {
                    newGoal = new EternalGoals();
                }
                else if (GoalAnswer == "3")
                {
                    newGoal = new ChecklistGoal();
                }
                else
                {
                    Console.WriteLine("Invalid Choice");
                }
                Console.WriteLine("Please enter a name for your goal:");
                string GoalName = Console.ReadLine();
                newGoal.SetName(GoalName);
                Console.WriteLine("Please enter a description of your goal:");
                newGoal.SetDesc(Console.ReadLine());
                Console.WriteLine("Please enter the goal points value:");
                string pointsString = Console.ReadLine();
                Int32.TryParse(pointsString, out int points);
                newGoal.SetPoints(points);
                if (newGoal is ChecklistGoal checklistGoal)
                {
                    Console.WriteLine("How many times does this goal need to be accomplished for a bonus? ");
                    string bonusTarget = Console.ReadLine();
                    Int32.TryParse(bonusTarget, out int target);
                    newGoal.SetGoalTarget(target);
                    Console.WriteLine("How many bonus points will you award?");
                    string bonusPoints = Console.ReadLine();
                    Int32.TryParse(bonusPoints, out int bonus);
                    newGoal.SetGoalBonus(bonus);
                }
                goals.Add(newGoal);
                Console.WriteLine("Goal added!");
                Console.Clear();
                Start();
            }
            else if (Answer == "2")
            {
                foreach (var goal in goals)
                {
                    Console.WriteLine(goal.GetStringRepresentation());
                }

            }
            else if (Answer == "3")
            {
                Console.WriteLine("Enter filename to save all Goals to (e.g., mygoals.csv):");
                string filename = Console.ReadLine();

                if (!filename.EndsWith(".csv"))
                {
                    filename += ".csv";
                }

                using (StreamWriter writer = new StreamWriter(filename))
                {
                    writer.WriteLine(totalPoints);
                    foreach (var goal in goals)
                    {
                        writer.WriteLine(goal.GetStringRepresentation());
                    }
                }


            }
            else if (Answer == "4")
            {
                Console.WriteLine("Please enter a filename to load: ");
                string name = Console.ReadLine();
                if (System.IO.File.Exists(name))
                {
                    string[] lines = System.IO.File.ReadAllLines(name);

                }
            }
            else if (Answer == "5")
            {
                if (goals.Count == 0)
                {
                    Console.WriteLine("No goals to record event for.");
                    return;
                }

                Console.WriteLine("Select a goal to mark as complete:");
                                for (int i = 0; i < goals.Count; i++)
                {
                    Console.WriteLine($"{i + 1}. {goals[i].GetDetailsString()}");
                }

                Console.Write("Enter the number of the goal: ");
                string input = Console.ReadLine();

                if (int.TryParse(input, out int index) && index >= 1 && index <= goals.Count)
                {
                    totalPoints += goals[index - 1].RecordEvent(); // Mark as complete
                    Console.WriteLine("Goal marked as complete!");
                }
                else
                {
                    Console.WriteLine("Invalid selection.");
                }

            }
            else
            {
                Console.WriteLine("INVALID CHOICE :(");
                Start();
            }
        }
    }
}