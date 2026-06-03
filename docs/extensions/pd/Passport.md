---
search:
  boost: 10.0
---

# Class: Passport 


_Information about passport_



<div data-search-exclude markdown="1">



URI: [pd:Passport](https://w3id.org/lmodel/dpv/pd/Passport)





```mermaid
 classDiagram
    class Passport
    click Passport href "../Passport/"
      OfficialID <|-- Passport
        click OfficialID href "../OfficialID/"
      
      
```





## Inheritance
* [External](External.md)
    * [Identifying](Identifying.md)
        * [OfficialID](OfficialID.md)
            * **Passport**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Passport](https://w3id.org/lmodel/dpv/pd/Passport) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Passport




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Passport |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Passport |
| native | pd:Passport |
| exact | dpv_pd:Passport, dpv_pd_owl:Passport |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Passport
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Passport
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about passport
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Passport
exact_mappings:
- dpv_pd:Passport
- dpv_pd_owl:Passport
is_a: OfficialID
class_uri: pd:Passport

```
</details>

### Induced

<details>
```yaml
name: Passport
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Passport
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about passport
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Passport
exact_mappings:
- dpv_pd:Passport
- dpv_pd_owl:Passport
is_a: OfficialID
class_uri: pd:Passport

```
</details></div>