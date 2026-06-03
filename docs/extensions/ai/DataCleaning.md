---
search:
  boost: 10.0
---

# Class: DataCleaning 


_Processing operation where data is cleaned, e.g. by detecting and_

_removing errors or unwanted records_



<div data-search-exclude markdown="1">



URI: [ai:DataCleaning](https://w3id.org/lmodel/dpv/ai/DataCleaning)





```mermaid
 classDiagram
    class DataCleaning
    click DataCleaning href "../DataCleaning/"
      DataPreparation <|-- DataCleaning
        click DataPreparation href "../DataPreparation/"
      
      
```





## Inheritance
* [DataOperation](DataOperation.md)
    * [DataPreparation](DataPreparation.md)
        * **DataCleaning**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:DataCleaning](https://w3id.org/lmodel/dpv/ai/DataCleaning) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Data Cleaning




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#DataCleaning |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:DataCleaning |
| native | ai:DataCleaning |
| exact | dpv_ai:DataCleaning, dpv_ai_owl:DataCleaning |
| close | iso42001:DataResource |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataCleaning
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#DataCleaning
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Processing operation where data is cleaned, e.g. by detecting and

  removing errors or unwanted records'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Data Cleaning
exact_mappings:
- dpv_ai:DataCleaning
- dpv_ai_owl:DataCleaning
close_mappings:
- iso42001:DataResource
is_a: DataPreparation
class_uri: ai:DataCleaning

```
</details>

### Induced

<details>
```yaml
name: DataCleaning
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#DataCleaning
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Processing operation where data is cleaned, e.g. by detecting and

  removing errors or unwanted records'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Data Cleaning
exact_mappings:
- dpv_ai:DataCleaning
- dpv_ai_owl:DataCleaning
close_mappings:
- iso42001:DataResource
is_a: DataPreparation
class_uri: ai:DataCleaning

```
</details></div>