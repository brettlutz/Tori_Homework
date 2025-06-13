using System.ComponentModel;
using MakingGoals;

namespace MakingGoals
{
    public class SimpleGoal : Goal
    {
        public override int RecordEvent()
        {
            _isCompleted = true;
            // add points to total
            return _points;
        }

    }
}