---
search:
  boost: 10.0
---

# Class: DataPoisoning 


_Attack trying to manipulate the training dataset_



<div data-search-exclude markdown="1">



URI: [ai:DataPoisoning](https://w3id.org/lmodel/dpv/ai/DataPoisoning)





```mermaid
 classDiagram
    class DataPoisoning
    click DataPoisoning href "../DataPoisoning/"
      RiskConcept <|-- DataPoisoning
        click RiskConcept href "../RiskConcept/"
      SecurityAttack <|-- DataPoisoning
        click SecurityAttack href "../SecurityAttack/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [SecurityAttack](SecurityAttack.md)
        * **DataPoisoning** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:DataPoisoning](https://w3id.org/lmodel/dpv/ai/DataPoisoning) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Data Poisoning




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#DataPoisoning |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:DataPoisoning |
| native | ai:DataPoisoning |
| exact | dpv_ai:DataPoisoning, dpv_ai_owl:DataPoisoning |
| close | iso42001:AIIncident |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataPoisoning
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#DataPoisoning
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Attack trying to manipulate the training dataset
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Data Poisoning
exact_mappings:
- dpv_ai:DataPoisoning
- dpv_ai_owl:DataPoisoning
close_mappings:
- iso42001:AIIncident
is_a: SecurityAttack
mixins:
- RiskConcept
class_uri: ai:DataPoisoning

```
</details>

### Induced

<details>
```yaml
name: DataPoisoning
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#DataPoisoning
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Attack trying to manipulate the training dataset
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Data Poisoning
exact_mappings:
- dpv_ai:DataPoisoning
- dpv_ai_owl:DataPoisoning
close_mappings:
- iso42001:AIIncident
is_a: SecurityAttack
mixins:
- RiskConcept
class_uri: ai:DataPoisoning

```
</details></div>