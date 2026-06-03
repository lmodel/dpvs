---
search:
  boost: 10.0
---

# Class: Output 


_Output from a technology_



<div data-search-exclude markdown="1">



URI: [tech:Output](https://w3id.org/lmodel/dpv/tech/Output)





```mermaid
 classDiagram
    class Output
    click Output href "../Output/"
      InputOutput <|-- Output
        click InputOutput href "../InputOutput/"
      

      Output <|-- OutputAction
        click OutputAction href "../OutputAction/"
      Output <|-- OutputData
        click OutputData href "../OutputData/"
      

      
```





## Inheritance
* [InputOutput](InputOutput.md)
    * **Output**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:Output](https://w3id.org/lmodel/dpv/tech/Output) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Output




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#Output |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:Output |
| native | tech:Output |
| exact | dpv_tech:Output, dpv_tech_owl:Output |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Output
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Output
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Output from a technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Output
exact_mappings:
- dpv_tech:Output
- dpv_tech_owl:Output
is_a: InputOutput
class_uri: tech:Output

```
</details>

### Induced

<details>
```yaml
name: Output
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Output
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Output from a technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Output
exact_mappings:
- dpv_tech:Output
- dpv_tech_owl:Output
is_a: InputOutput
class_uri: tech:Output

```
</details></div>