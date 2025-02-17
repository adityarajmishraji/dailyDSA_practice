public class job {
    // Properties
    private int id;
    private String profile;
    private String tech;
    private String desc; // Added missing description field

    // Default constructor
    public job() {
    }

    // Parameterized constructor
    public job(int id, String profile, String tech, String desc) {
        this.id = id;
        this.profile = profile;
        this.tech = tech;
        this.desc = desc;
    }

    // Getters and Setters
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getProfile() {
        return profile;
    }

    public void setProfile(String profile) {
        this.profile = profile;
    }

    public String getTech() {
        return tech;
    }

    public void setTech(String tech) {
        this.tech = tech;
    }

    public String getDesc() {
        return desc;
    }

    public void setDesc(String desc) {
        this.desc = desc;
    }

    // Overriding toString() method
    @Override
    public String toString() {
        return "job{" +
                "id=" + id +
                ", profile='" + profile + '\'' +
                ", tech='" + tech + '\'' +
                ", desc='" + desc + '\'' +
                '}';
    }
}
//run time error
