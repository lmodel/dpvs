---
search:
  boost: 10.0
---

# Class: OfficialID 


_Information about an official identifier or identification document_



<div data-search-exclude markdown="1">



URI: [pd:OfficialID](https://w3id.org/lmodel/dpv/pd/OfficialID)





```mermaid
 classDiagram
    class OfficialID
    click OfficialID href "../OfficialID/"
      Identifying <|-- OfficialID
        click Identifying href "../Identifying/"
      

      OfficialID <|-- Passport
        click Passport href "../Passport/"
      

      
```





## Inheritance
* [External](External.md)
    * [Identifying](Identifying.md)
        * **OfficialID**
            * [Passport](Passport.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:OfficialID](https://w3id.org/lmodel/dpv/pd/OfficialID) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Official ID




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#OfficialID |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:OfficialID |
| native | pd:OfficialID |
| exact | dpv_pd:OfficialID, dpv_pd_owl:OfficialID |
| related | svd:Government |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: OfficialID
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#OfficialID
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about an official identifier or identification document
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Official ID
exact_mappings:
- dpv_pd:OfficialID
- dpv_pd_owl:OfficialID
related_mappings:
- svd:Government
is_a: Identifying
class_uri: pd:OfficialID

```
</details>

### Induced

<details>
```yaml
name: OfficialID
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#OfficialID
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about an official identifier or identification document
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Official ID
exact_mappings:
- dpv_pd:OfficialID
- dpv_pd_owl:OfficialID
related_mappings:
- svd:Government
is_a: Identifying
class_uri: pd:OfficialID

```
</details></div>