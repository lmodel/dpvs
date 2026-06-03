---
search:
  boost: 10.0
---

# Class: OutputData 


_Data that is produced as an output from a technology_



<div data-search-exclude markdown="1">



URI: [tech:OutputData](https://w3id.org/lmodel/dpv/tech/OutputData)





```mermaid
 classDiagram
    class OutputData
    click OutputData href "../OutputData/"
      Output <|-- OutputData
        click Output href "../Output/"
      
      
```





## Inheritance
* **OutputData** [ [Output](Output.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:OutputData](https://w3id.org/lmodel/dpv/tech/OutputData) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Output Data




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#OutputData |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:OutputData |
| native | tech:OutputData |
| exact | dpv_tech:OutputData, dpv_tech_owl:OutputData |
| close | iso22989:Data |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: OutputData
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#OutputData
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Data that is produced as an output from a technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Output Data
exact_mappings:
- dpv_tech:OutputData
- dpv_tech_owl:OutputData
close_mappings:
- iso22989:Data
mixins:
- Output
class_uri: tech:OutputData

```
</details>

### Induced

<details>
```yaml
name: OutputData
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#OutputData
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Data that is produced as an output from a technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Output Data
exact_mappings:
- dpv_tech:OutputData
- dpv_tech_owl:OutputData
close_mappings:
- iso22989:Data
mixins:
- Output
class_uri: tech:OutputData

```
</details></div>