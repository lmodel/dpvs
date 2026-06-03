---
search:
  boost: 10.0
---

# Class: DataEnrichment 


_Processing operation where data is enriced, e.g. by adding additional_

_data that increases its value or usefulness_



<div data-search-exclude markdown="1">



URI: [ai:DataEnrichment](https://w3id.org/lmodel/dpv/ai/DataEnrichment)





```mermaid
 classDiagram
    class DataEnrichment
    click DataEnrichment href "../DataEnrichment/"
      DataPreparation <|-- DataEnrichment
        click DataPreparation href "../DataPreparation/"
      
      
```





## Inheritance
* [DataOperation](DataOperation.md)
    * [DataPreparation](DataPreparation.md)
        * **DataEnrichment**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:DataEnrichment](https://w3id.org/lmodel/dpv/ai/DataEnrichment) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Data Enrichment




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#DataEnrichment |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:DataEnrichment |
| native | ai:DataEnrichment |
| exact | dpv_ai:DataEnrichment, dpv_ai_owl:DataEnrichment |
| close | iso42001:DataResource |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataEnrichment
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#DataEnrichment
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Processing operation where data is enriced, e.g. by adding additional

  data that increases its value or usefulness'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Data Enrichment
exact_mappings:
- dpv_ai:DataEnrichment
- dpv_ai_owl:DataEnrichment
close_mappings:
- iso42001:DataResource
is_a: DataPreparation
class_uri: ai:DataEnrichment

```
</details>

### Induced

<details>
```yaml
name: DataEnrichment
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#DataEnrichment
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Processing operation where data is enriced, e.g. by adding additional

  data that increases its value or usefulness'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Data Enrichment
exact_mappings:
- dpv_ai:DataEnrichment
- dpv_ai_owl:DataEnrichment
close_mappings:
- iso42001:DataResource
is_a: DataPreparation
class_uri: ai:DataEnrichment

```
</details></div>