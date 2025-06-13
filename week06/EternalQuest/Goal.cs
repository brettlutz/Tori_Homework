using System.ComponentModel;
using MakingGoals;

namespace MakingGoals
{
    public abstract class Goal
    {
        protected string _shortName;
        protected string _description;
        protected bool _isCompleted = false;
        protected int _goalBonus;
        protected int _goalTarget;
        protected int _eventsCompleted;
        protected int _points;

        public void SetName(string ShortName)
        {
            _shortName = ShortName;
        }
        public string GetName()
        {
            return _shortName;
        }
        public void SetDesc(string Description)
        {
            _description = Description;
        }
        public string GetDesc()
        {
            return _description;
        }

        public void SetPoints(int Points)
        {
            _points = Points;
        }

        public int GetPoints()
        {
            return _points;
        }

        public void SetGoalBonus(int bonus)
        {
            _goalBonus = bonus;
        }
        public int GetGoalBonus()
        {
            return _goalBonus;
        }

        public void SetGoalTarget(int target) {
            _goalTarget = target;
        }
        public int GetGoalTarget()
        {
            return _goalTarget;
        }
        public void SetEventsCompleted(int completed)
        {
            _eventsCompleted = completed;
        }
        public int GetEventsCompleted()
        {
            return _eventsCompleted;
        }

        public string goal()
        {
            return $"{_shortName}, {_description} this activity earns you {_points}";
        }
        public abstract int RecordEvent();
        public string GetStatusIcon()
        {
            return _isCompleted ? "[X]" : "[ ]";
        }
        public virtual void MarkComplete()
        {
            _isCompleted = true;
        }

        public string GetDetailsString()
        {
            return $"{GetStatusIcon()} {_shortName} - {_description}";
        }

        public virtual string GetStringRepresentation()
        {
            return $"{_shortName}, {_description} this activity earns you {_points}";
        }
    }

}
