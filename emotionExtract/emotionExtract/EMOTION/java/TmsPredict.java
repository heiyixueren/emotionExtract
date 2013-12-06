package tms;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

//import org.apache.commons.logging.Log;
//import org.apache.commons.logging.LogFactory;
//import org.jsoup.helper.StringUtil;


public class TmsPredict  {
	
	private List<TmsModel> models; 
//	protected static final Log log = LogFactory.getLog(MsgClassifier.class);
	/**
	 * ���캯������Ҫ����ģ�����ڵ�·���Լ������ļ�������
	 * @param paths
	 * @param configNames
	 */
	public TmsPredict(String[] paths,String[] configNames){
		models =  new ArrayList<TmsModel>();
		for(int i =0;i<paths.length;i++){
			models.add(new TmsModel(paths[i],configNames[i]));
		}
	}
	/**
	 * ���캯������Ҫ����ģ�����ڵ�·���������ļ�����Ĭ��Ϊtms.config
	 * @param paths
	 * @param configNames
	 */
	
	public TmsPredict(String[] paths){
		models =  new ArrayList<TmsModel>();
		for(int i =0;i<paths.length;i++){
			models.add(new TmsModel(paths[i],"tms.config"));
		}
	}
	
	/**
	 * �����������ڳ���1�����յ�List<String>���͵����ݡ�
	 * Ȼ���������е�ģ�ͽ���Ԥ�����
	 * @param text ������ı���List���汣��ÿ���ʡ�
	 * @return ����SvmResult���͵Ľ����
	 */
	
	public SvmResult[] calScore(List<String> text){
		int k = models.size();
		SvmResult[] result = new SvmResult[k];
		for(int i=0;i<k;i++){
			TmsModel tmsModel = models.get(i);
			result[i] = this.calSigleTmsScore(text,tmsModel);
		}
		return result;

	}
	
//	/**
//	 * �����������ڳ���2�����յ�String���͵����ݡ�
//	 * Ȼ���������е�ģ�ͽ���Ԥ�����
//	 * @param text ������ı�
//	 * @return ����SvmResult���͵Ľ����
//	 */
//	
//	public SvmResult[] calScore(String doc){
//		String text = this.preProcContent(doc);
//		List<String> words = this.participle(text);
//		return this.calScore(words);
//	}
	
	/**
	 * �����������ڳ���3������һ���ַ�����������ִʵķָ����š�
	 * Ȼ���������е�ģ�ͽ���Ԥ�����
	 * @param line ������ı�
	 * @param str_splitTag �ִʺ��ı��ķָ���š�
	 * @return ����SvmResult���͵Ľ����
	 */
	
	public SvmResult[] calScore(String text,String str_splitTag){
		String[] line = text.split(str_splitTag);
		List<String > words = new ArrayList<String>();
		for(String s:line)
			words.add(s);
		return this.calScore(words);

	}
	
	/**
	 * �����������ڳ���4���������룬�Լ����ַָ���ź�ָ���
	 * ����������Զ����е�ģ���ر��ƣ���Ϊ��ͬ��ģ�Ϳ��ܼ����ֶβ�ͬ
	 * Ȼ���������е�ģ�ͽ���Ԥ�����
	 * @param line ������ı�
	 * @param tc_splitTag �����ı���Ϊ�������֣���������֮��ķָ����
	 * @param str_splitTag �ִʺ��ı��ķָ���š�
	 * @param str_connentTag ���Ҫ������ַ���һ��Ԥ�⣬��Ҫ�������ӷ���������һ��ʵ����str_splitTag��str_connentTag��һ��������������java�����߲�����ͬ ^ \\^
	 * @return
	 */
	public SvmResult[] calScore(String line,int[][] indexes,String tc_splitTag,String str_splitTag,String str_connentTag){
		String []input_text = line.split(tc_splitTag);
		int k = models.size();
		SvmResult[] result = new SvmResult[k];
		for(int i=0;i<k;i++){
			int[] index = indexes[i];
			TmsModel tmsModel = models.get(i);
			String text = mergeText(input_text, index,str_connentTag);
			List<String> words = new ArrayList<String>();
			for(String s:text.split(str_splitTag))
				words.add(s);
			result[i] = calSigleTmsScore(words,tmsModel);
		}
		return result;

	}
	
//	protected String preProcContent(String doc) {
//		//ȥ��html��ǩ
//		doc=FilterUtil.extractHtmlContextNotNull(doc);
//		//ȥ�������ַ�
//		String specChars="�٧�ԧ���ܧ�ݧ�Q��R��������ڧ�ۧ�שU\"��# ��!&����'��$��%���*��+���(���)��.��/��,�զ�-�P;:?>=<�t�u�Ωr�s�ĩq��@�o�p�O�{�|���y�өz�w�ũx�ɡȡҡߡ�˧���æ��觱�姰�n]�ק�\\�m�l_�k^�j�i���h[����������`�����᧴�ǡ⧲�������ʧ����ݩ��ܨM�۩��ک~��}�ੁ�Ƨߩ��ިN��~��}��|��{�١̧֧ա���������ͨS���ѡ¨��������������������������������ޣܣݨ������������Ш��������������W���V�����C�\���D����������������F�����A�@�B�������������é©������������������������������������������������ߢ��ޢ��ݢ��ܢ��㢤�⢣�ᢢ�ࢡ�ש֩թԩ۩ک٢��آ����΢��Ϣ��̢��͢�Ң��Ӣ�Т�ѩƩǩĩũʢ����˩Ȣ����ɩ@�a�`�c�B�A�b�]�\�_��^�Y�X�[�Z�U�T�W�V����G�����H������硣�w���v���u���t�r���s���p���q���n���o���l���m�j�k�h�i�f���g�d�e���̦ͦΨ��Ϩ��Ȩ��ɦʦ˦ĦŦƦǨx�z�y�|���{���~�}�������������������������������������������K�L���������I�J������𨐦ب��ר����ҦѦЦ֦զԦ�";
//		doc=com.taobao.tbctu.help.TextHelper.skipChars(doc,specChars);
//		return doc;
//	}
//
//	protected List<String> participle(String doc) {
//		List<String> words=new ArrayList<String>();
//		if(StringUtil.isBlank(doc))
//			return words;	
//		words= KFCParticiple(doc);		
//		return words;
//	}

	/**
	 * �Ѽ����ֿ����ı������������������ӷ���Ҫ���Ժ�ָ�ķ�����ͬ
	 * @param original_text
	 * @param indexes
	 * @param str_splitTag
	 * @return
	 */
	public String mergeText(String[] original_text,int[] indexes,String str_connentTag){
		String text="";
		for(int i =0;i<indexes.length;i++)
			text+=str_connentTag+original_text[indexes[i]];
		return text;
	}
	
	/**
	 * ����SVMģ�͵ķ���.֧�ֶ�ģ��
	 * @param text_arr  ������ı�������ΪString[]��ʽ
	 * @param dic �ֵ�
	 * @param model ģ��
	 * @return
	 */
	public SvmResult calSigleTmsScore(List<String> text,TmsModel tmsModel){
		SvmModel svmModel = tmsModel.getModel();
        int label;
		double score;
        String descr;
		int nr_class = svmModel.getNrClass();
		double[] des_values =new double[nr_class*(nr_class-1)/2];
		SvmNode[] nodeList = consProForSVM(text, tmsModel);
		if (nodeList == null){ //������ı��Ĵ��ڴʵ� ��û�г��ֹ����򷵻�һ����С��ֵ��
			return new SvmResult(0,0,"������̫��");
		}	
		label = svmModel.predictValues(svmModel,nodeList,des_values);
		score = svmModel.sumPreValue(des_values);
		descr = tmsModel.getLabelDescr(label);
        return new SvmResult(label,score,descr);

	}

	/**
	 * ����������ı����Լ�����Ĵʵ䣬����SVMģ��(libsvm,liblinear)���ض�����
	 * �ú�����Ŀ�ľ��ǹ����ı������������������й�һ���������Ǵ˴�Ϊ�����Ч�ʣ�����Map����Vector��ֻ�洢��0ֵ��
	 * @param text ����洢��Ϊһ�����Ĵ�
	 * @param dic ���ô洢��Ϊ�ʵ䣬String Ϊ�ʣ�IntegerΪ��Id
	 * @return ���ص���SVM�ض�������ṹ,TmsNode[]
	 */
	
	public SvmNode[] consProForSVM(List<String> text,TmsModel tmsModel){
		Map<Integer,Double> feature_map = new HashMap<Integer,Double>();
		Map<String,Integer> dic = tmsModel.getDic();
		//�����ı���ÿ���ʶ�Ӧ��ʵ��λ�ã��Լ���Ӧ�Ĵ�Ƶ��
		for(int i =0;i<text.size();i++){
			String term = (text.get(i).toString()).trim();
	        if (dic.containsKey(term)){ //��ѯdic���Ƿ�����ô�
	        	int index = dic.get(term); //�������������feature_map����Ӧλ�ü�1
	        	if (feature_map.containsKey(index)){ //������������һ���Ǹô��Ѿ��ڴʵ��У�
	        		double  count =  feature_map.get(index);
	        		feature_map .put(index, count+1.0);
	        	}
	        	else  //��һ���Ǹô�δ�ڴʵ���
	        		feature_map .put(index, 1.0);
	        }
		}
		//��������Ȩ�صĹ�ʽ���¼������������е�Ȩ��
		//���ݵ��Ǿֲ���ʽ��ȫ������
		Object[] keys = feature_map.keySet().toArray();
		for(int i = 0;i<keys.length;i++){
			feature_map.put((Integer)keys[i],tmsModel.getLocalFun().Fun(feature_map.get(keys[i]))*tmsModel.getGlobalWeight().get(keys[i]) );
		}

		//������ĵ�����������ģ
		double vec_sum = 0.0;

		for(int i=0;i<keys.length;i++){
			vec_sum += feature_map.get(keys[i])*feature_map.get(keys[i]);
		}
	    double vec_length=Math.sqrt(vec_sum);
	    
	    //��һ��������SVMģ�͵�����
	    SvmNode[] x=null;
	    Arrays.sort(keys); //��feature_map�е�key����������Ҫ��Ϊ�˱�֤�����SVM��ʽ��Index���������С�
	    if(vec_length>0){
	    	int m = keys.length;
			 x= new SvmNode[m]; //SVMģ�͵������ʽ
			/**�˴�Ϊ����SVM�����ʽ�ľ���**/
			//�����ı��еĴʳ��ֵĴ�Ƶ��
			for(int j=0;j<m;j++)
			{
				x[j] = new SvmNode();
				x[j].index = (Integer)keys[j];
				x[j].value = (double)( feature_map.get(keys[j])/vec_length); //�˴�Ҫ���й�һ��
			}
	    }
		
	    return x;
	}
	
	/**
	 * �ִ�
	 * @param doc
	 * @return
	 */
//	protected List<String> KFCParticiple(String doc){
//		
//		
//		if(StringUtil.isBlank(doc))
//			return new ArrayList<String>();
//		
//		// ʹ��kfc �Դ��ִʺ���
//		WordPartition wp=new WordPartitionAdapter();
//		List<String> words=wp.partition(doc);
//		return words;
//		
//	}
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		//��ʹ��KFC�ķִʣ������Ѿ��ֺôʵ������Գ�����в��ԡ�
		String[] paths={"G:/x��Ŀ/Taobao/������������/ģ��/�������Ӽ��/weijin_all_kinds/model","G:/x��Ŀ/Taobao/������������/ģ��/�������Ӽ��/weijin_all_kinds/model","G:/x��Ŀ/Taobao/������������/ģ��/�������Ӽ��/weijin_all_kinds/model","G:/x��Ŀ/Taobao/������������/ģ��/�������Ӽ��/weijin_all_kinds/model"};
		String[] configNames ={"lineartitle.config","lineartitle_content.config","svmtitle.config","svmtitle_content.config"};
		int[][] indexes = {{4},{4,5},{4},{4,5}};
		TmsPredict libsvm = new TmsPredict(paths,configNames);
		
		String in_filename = "G:/x��Ŀ/Taobao/������������/ģ��/�������Ӽ��/weijin_all_kinds/weijin_all_kinds_1116.train"; //�����ļ�
		String tc_splitTag="\t"; //��������ݸ�������֮��ķָ����
		String str_splitTag ="\\^"; //��������ݾ����ִʺ󣬸����ʵķָ����
		String str_connentTag="^";
		String out_filename = "G:/x��Ŀ/Taobao/������������/ģ��/�������Ӽ��/weijin_all_kinds/result.txt"; //���������ļ�			
	
		try {	
			InputStream in = new FileInputStream(in_filename);				
			BufferedReader input = new BufferedReader(new InputStreamReader(in,"UTF-8"));
			PrintWriter output = new PrintWriter(out_filename);
			while(true){
				String line = input.readLine();	
				if(line == null) 
					break;
				String[] text  = line.split(tc_splitTag);
				SvmResult[] post_sc = libsvm.calScore(line,indexes,tc_splitTag,str_splitTag,str_connentTag); //����÷֣�����֣�����+���ݷ֣�
				//SvmResult[] post_sc = libsvm.calScore(line, str_splitTag); //����÷֣�����֣�����+���ݷ֣�
				output.print(text[2]+"\t"+text[0]+"\t");
				for(SvmResult score :post_sc)
					output.print(score.getLabel()+"\t"+score.getScore()+"\t");
				
				output.println();
			}
			input.close();
			output.close();	
		}catch(IOException e){
			e.printStackTrace();
		}
	}

}
