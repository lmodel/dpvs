---
search:
  boost: 10.0
---

# Class: ProvidedAsFixedUse 


_Technology provided for using a fixed number of times_



<div data-search-exclude markdown="1">



URI: [tech:ProvidedAsFixedUse](https://w3id.org/lmodel/dpv/tech/ProvidedAsFixedUse)





```mermaid
 classDiagram
    class ProvidedAsFixedUse
    click ProvidedAsFixedUse href "../ProvidedAsFixedUse/"
      ProvisionMethod <|-- ProvidedAsFixedUse
        click ProvisionMethod href "../ProvisionMethod/"
      
      
```





## Inheritance
* [ProvisionMethod](ProvisionMethod.md)
    * **ProvidedAsFixedUse**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:ProvidedAsFixedUse](https://w3id.org/lmodel/dpv/tech/ProvidedAsFixedUse) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Provided as Fixed UseProvision




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#ProvidedAsFixedUse |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:ProvidedAsFixedUse |
| native | tech:ProvidedAsFixedUse |
| exact | dpv_tech:ProvidedAsFixedUse, dpv_tech_owl:ProvidedAsFixedUse |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ProvidedAsFixedUse
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#ProvidedAsFixedUse
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Technology provided for using a fixed number of times
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Provided as Fixed UseProvision
exact_mappings:
- dpv_tech:ProvidedAsFixedUse
- dpv_tech_owl:ProvidedAsFixedUse
is_a: ProvisionMethod
class_uri: tech:ProvidedAsFixedUse

```
</details>

### Induced

<details>
```yaml
name: ProvidedAsFixedUse
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#ProvidedAsFixedUse
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Technology provided for using a fixed number of times
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Provided as Fixed UseProvision
exact_mappings:
- dpv_tech:ProvidedAsFixedUse
- dpv_tech_owl:ProvidedAsFixedUse
is_a: ProvisionMethod
class_uri: tech:ProvidedAsFixedUse

```
</details></div>