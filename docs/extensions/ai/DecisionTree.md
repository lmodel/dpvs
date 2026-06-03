---
search:
  boost: 10.0
---

# Class: DecisionTree 


_Technique for which inference is encoded as paths from the root to a_

_leaf node in a tree structure_



<div data-search-exclude markdown="1">



URI: [ai:DecisionTree](https://w3id.org/lmodel/dpv/ai/DecisionTree)





```mermaid
 classDiagram
    class DecisionTree
    click DecisionTree href "../DecisionTree/"
      Technique <|-- DecisionTree
        click Technique href "../Technique/"
      MachineLearning <|-- DecisionTree
        click MachineLearning href "../MachineLearning/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Technique](Technique.md)
        * [MachineLearning](MachineLearning.md)
            * **DecisionTree** [ [Technique](Technique.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:DecisionTree](https://w3id.org/lmodel/dpv/ai/DecisionTree) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Decision Tree




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 3.3.2 |
| upstream_iri | https://w3id.org/dpv/ai/owl#DecisionTree |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:DecisionTree |
| native | ai:DecisionTree |
| exact | dpv_ai:DecisionTree, dpv_ai_owl:DecisionTree |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DecisionTree
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.3.2
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#DecisionTree
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Technique for which inference is encoded as paths from the root to a

  leaf node in a tree structure'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Decision Tree
exact_mappings:
- dpv_ai:DecisionTree
- dpv_ai_owl:DecisionTree
is_a: MachineLearning
mixins:
- Technique
class_uri: ai:DecisionTree

```
</details>

### Induced

<details>
```yaml
name: DecisionTree
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.3.2
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#DecisionTree
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Technique for which inference is encoded as paths from the root to a

  leaf node in a tree structure'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Decision Tree
exact_mappings:
- dpv_ai:DecisionTree
- dpv_ai_owl:DecisionTree
is_a: MachineLearning
mixins:
- Technique
class_uri: ai:DecisionTree

```
</details></div>