
class ExchageRate:

    ##this will fatch data from the dictionary
    dict_studentDB ={}
    list_lru= []
    def memcachedFetch(self,studentId):
        studentData = dict.get(studentId, default=None)
        if student_data == None:
            # student_data should have been fatch from database adn the result should return and store in the memory
            student_data = 'detail of the sutdent' + studentId
            memcachedAdd(self,studentId,student_data)
            list_lru.append(studentId)
        else
            dict_lru.remove(studentId)
            list_lru.append(studentId)

        return student_data

    # This will add record to the student database by checking the total record did not
    # increase the no of define
    def memcachedAdd(self,studentId,student_data):
        if dict_studentDB.len() == 10:
            memcachedDelete()

        dict_studentDB[studentId] = student_data

    def memcachedDelete(self):
        # there could be multiple record havin same m
        del dict_studentDB[list_lru[0]]


def main():

    #This will create table to store the data in the database
    conn = sqlite3.connect('spider.sqlite3')
    cur = conn.cursor()



    #start_date is always 2 year prior date from the end date entered
    start_date = end_date - datetime.timedelta(days=730)
    #For testing I have use only last 5 days
    #start_date = end_date - datetime.timedelta(days=5)
    #For 2 years data
    #start_date = end_date - datetime.timedelta(days=730)
    print("Base currency --> ",base)
    print("Start date --> ",start_date)
    print("End date --> ",end_date)



if __name__ == '__main__':
    main()
